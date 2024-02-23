# -*- coding: utf-8 -*-
import psycopg2, time
from psycopg2 import pool

class WEB_DB:
    def __init__(self, config, init_pool_num=5, max_pool_num=20):
        self.config = config
        self.dbConnPool = None        
        try:
            self.dbConnPool = psycopg2.pool.ThreadedConnectionPool(
                init_pool_num, max_pool_num, 
                user=self.config["database"]["user"],
                password=self.config["database"]["password"],
                host=self.config["database"]["host"],
                port=self.config["database"]["port"],
                database=self.config["database"]["dbName"])
            
            if (self.dbConnPool):
                print("[INFO] Connection pool created successfully using ThreadedConnectionPool")
            
        except (Exception, psycopg2.DatabaseError) as error:
            print("[ERROR] " + str(error))
            self.dbConnPool= None
    
    def query_db(self, conn, sqlQuery, *args):
        rows = None
        try:            
            cur = conn.cursor()
            cur.execute(sqlQuery, args)
            rows = cur.fetchall()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("[ERROR] " + str(error))
            return None, error
        finally:
            if cur is not None:
                cur.close()

        return rows, None
    
    def exe_sql_db(self, conn, commit, sqlInsert, *args):
        cur = conn.cursor()
        try:
            cur.execute(sqlInsert, args)
        except (Exception, psycopg2.DatabaseError) as error:
            print("[ERROR] " + str(error))
            return False, error
        finally:
            if commit:
                conn.commit()
            if cur is not None:
                cur.close()

        return True, None    
    
    def create_clientid_profile(self, clientid, username, password):
        status = False
        message = None        
        insertSQL1 = 'INSERT INTO public.mqtt_user(clientid, username, password) values (%s, %s, %s)'        
        insertSQL2 = 'INSERT INTO public.clientid_profile(clientid, created_at) values (%s, %s)'
        dbConn = self.dbConnPool.getconn()
        if (dbConn):
            status, message = self.exe_sql_db(dbConn, True, insertSQL1, clientid, username, password)
            if (status):                
                status, message = self.exe_sql_db(dbConn, True, insertSQL2, clientid, time.time())
            self.dbConnPool.putconn(dbConn)
        return status, message
    
    def get_clientid_profile(self, clientid=None):
        matchClientList = []
        if clientid == None:
            selectSQL = 'SELECT clientid, connection_status, model_name, serial_number, host_name, tpe_version, firmware_version, bios_version, created_at, profile_updated_at, connection_status_updated_at FROM public.clientid_profile order by clientid'
        else:           
            selectSQL = 'SELECT clientid, connection_status, model_name, serial_number, host_name, tpe_version, firmware_version, bios_version, created_at, profile_updated_at, connection_status_updated_at FROM public.clientid_profile where clientid=%s order by clientid'
        try:
            dbConn = self.dbConnPool.getconn()
            if (dbConn):
                clientidRows, error = self.query_db(dbConn, selectSQL , clientid)
                self.dbConnPool.putconn(dbConn)                
                for client in clientidRows:
                    item = {
                        "clientid": client[0],
                        "connection_status": client[1],
                        "model_name": client[2],
                        "serial_number": client[3],
                        "host_name": client[4],
                        "tpe_version": client[5],
                        "firmware_version": client[6],
                        "bios_version": client[7],
                        "created_at": client[8],
                        "profile_updated_at": client[9],
                        "connection_status_updated_at": client[10]
                    }  
                    matchClientList.append(item)  
            else:
                print("[ERROR] dbConn fail")
                
            return matchClientList, False
        except Exception as e:
            return str(e), True
    
    def update_clientid_profile(self, clientid, model_name, serial_number, host_name, tpe_version, firmware_version, bios_version):
        status = False
        message = None
        updateSQL = 'UPDATE public.clientid_profile set model_name=%s, serial_number=%s, host_name=%s, tpe_version=%s, firmware_version=%s, bios_version=%s, profile_updated_at=%s where clientid = %s'
        dbConn = self.dbConnPool.getconn()
        if (dbConn):
            status, message = self.exe_sql_db(dbConn, True, updateSQL, model_name, serial_number, host_name, tpe_version, firmware_version, bios_version, time.time(), clientid)
            self.dbConnPool.putconn(dbConn)
        return status, message

    def delete_clientid_profile(self, clientid):
        status = False
        message = None
        deleteQuery = 'DELETE FROM public.clientid_profile where clientid=%s'
        dbConn = self.dbConnPool.getconn()
        if (dbConn):
            status, message = self.exe_sql_db(dbConn, True, deleteQuery, clientid)
            self.dbConnPool.putconn(dbConn)
        return status, message
               
    def update_clientid_profile_connection_status(self, clientid, connectionStatus, updated_at):
        status = False
        message = None
        updateSQL = 'UPDATE public.clientid_profile set connection_status = %s, connection_status_updated_at = %s where clientid = %s'
        dbConn = self.dbConnPool.getconn()
        if (dbConn):
            if updated_at != None:
                update_ts = updated_at/1000
            else:
                update_ts = time.time()
            status, message = self.exe_sql_db(dbConn, True, updateSQL, connectionStatus, update_ts, clientid)
            self.dbConnPool.putconn(dbConn)
        return status, message
    
    def get_operation_category(self):
        categoryList = [] 
        selectSQL = 'SELECT id, name FROM public.dm_category'
        try:
            dbConn = self.dbConnPool.getconn()
            if (dbConn):
                categoryRows, error = self.query_db(dbConn, selectSQL)
                self.dbConnPool.putconn(dbConn) 
                for category in categoryRows:
                    item = {
                        "id": category[0],
                        "name": category[1]
                    }  
                    categoryList.append(item)  
            else:
                print("[ERROR] dbConn fail")
                
            return categoryList, False
        except Exception as e:
            return str(e), True
    
    def get_operation_by_category(self, categoryid):
        operationList = [] 
        selectSQL = 'SELECT id, categoryid, name, command FROM public.dm_operation where categoryid = %s'
        try:
            dbConn = self.dbConnPool.getconn()
            if (dbConn):
                operationRows, error = self.query_db(dbConn, selectSQL, categoryid)
                self.dbConnPool.putconn(dbConn) 
                for operation in operationRows:
                    item = {
                        "id": operation[0],
                        "categoryid": operation[1],
                        "name": operation[2],
                        "command": operation[3]
                    }  
                    operationList.append(item)  
            else:
                print("[ERROR] dbConn fail")
                
            return operationList, False
        except Exception as e:
            return str(e), True


    
        

