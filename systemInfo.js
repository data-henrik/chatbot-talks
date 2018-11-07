var ibmdb = require('ibm_db');
/**
  * Retrieve event information by searching the shortname
  *
  * Written by Henrik Loeser
  */

function fetchSystemInfo(dsn) {
 try {
    var conn=ibmdb.openSync(dsn);
    // Search for exact match only, could be extended with lIKE
    var data=conn.querySync("select SUBSTR(NAME,1,20) AS NAME, SUBSTR(VALUE,1,10) AS VALUE FROM SYSIBMADM.ENV_SYS_RESOURCES ");
    conn.closeSync();
    var resString="System Information:\n";
    for (var i=0;i<data.length;i++) {
      resString+="name: "+data[i]['NAME']+" value: "+data[i]['VALUE']+"\n";
    }
    // Return both generated string and data
    return {result : resString, data : data};
 } catch (e) {
     return { dberror : e }
 }
}

function main({ __bx_creds: {dashDB:{dsn}}}) {
	return fetchSystemInfo(dsn);
}
