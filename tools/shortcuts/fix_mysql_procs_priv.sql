-- Fix for: Cannot load from mysql.procs_priv. The table is probably corrupted!
-- Run this after starting MySQL:
--   mysql -u root -padmin -h 127.0.0.1 -P 3306 < tools/shortcuts/fix_mysql_procs_priv.sql

REPAIR TABLE mysql.procs_priv;
REPAIR TABLE mysql.columns_priv;
REPAIR TABLE mysql.tables_priv;
REPAIR TABLE mysql.db;
REPAIR TABLE mysql.user;
FLUSH PRIVILEGES;

SELECT 'mysql.procs_priv repair complete' AS status;
