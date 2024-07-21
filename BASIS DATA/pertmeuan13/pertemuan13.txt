use project_db;
select Host, user, Select_priv, Process_priv, ssl_type, max_updates from mysql.user where user = 'me';
select Host, db, user, Select_priv, Update_priv from mysql.db where user = 'me';
select host, db, Select_priv, Update_priv from mysql.host;
/*https://dev.mysql.com/doc/refman/8.0/en/grant-tables.html dari website tersebut tabel dari host tidak ada*/

create user 'user1'@'localhost';

grant all on *.* to 'user1'@'localhost'; /*belum menggunakan password*/
select Host, user, Select_priv, Update_priv from mysql.user where user = 'user1';
grant select,update on priject_db.* to 'user1'@'localhost';
select Host, user, Select_priv, Update_priv from mysql.user where user = 'user1';
select Host, db,user, Select_priv, Update_priv from mysql.db where user = 'user1';

show grants for 'user1'@'localhost';

set password for 'user1'@'localhost' = '123';

Flush privileges;

/*grant select,update
on project_db.*
to 'user1'@'localhost' identified by '123'
with grant option max_queries_per_hour 50 max_updates_per_hour 50;*/
/* pertintah diatas tidak dapat dilaksanakan karena terdapat error pada identified. dari sumber yang saya baca seharusnya identified berada pada saat create user*/
/* perintah max_queries dan max_updates seharusnya dipanggil melalui alter user*/
grant select,update
on project_db.*
to 'user1'@'localhost'
WITH GRANT OPTION;

alter user 'user1'@'localhost' with max_queries_per_hour 50 max_updates_per_hour 50;

revoke all privileges,grant option from 'user1'@'localhost';
revoke select,update,grant option on project_db.* from 'user1'@'localhost';
/* sudah tidak ada grant dari user1 */

drop user'user1'@'localhost';


/* kesimpulan */
/* dengan menggunakan perintah grant dapat memberikan suatu hak kepada user dengan perintah ini juga dapat memberikan opsi khusus pada hak yang akan diberikan*/
/* dengan menggunkan perintah revoke dapat menghapus hak dan opsi dari suatu user*/
/* table yang ada pada mysql:
user: User accounts, static global privileges, and other nonprivilege columns.

global_grants: Dynamic global privileges.

db: Database-level privileges.

tables_priv: Table-level privileges.

columns_priv: Column-level privileges.

procs_priv: Stored procedure and function privileges.

proxies_priv: Proxy-user privileges.

default_roles: Default user roles.

role_edges: Edges for role subgraphs.

password_history: Password change history.*/