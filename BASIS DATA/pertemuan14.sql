use pertemuan9;

/* untuk membuat cursor, hal pertama yang dilakukan adalah membuat stored procedure */

CREATE procedure dosen_cur()
begin
    declare done int default 0;
    declare nama varchar(50);
    declare email varchar(50);
    declare dosen_cursor cursor for select nama_dosen,email_dosen from dosen1;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    open dosen_cursor;

    read_loop: loop
        fetch dosen_cursor into nama,email;
        if done then
            leave read_loop;
        end if;
        SELECT nama as nama_dosen,email as email_dosen;
    end loop;
    close dosen_cursor;
end;


call dosen_cur;

CREATE trigger tambah_dosen after insert on dosen1
for each row
begin
    insert into dosen2(id_dosen,nama_depan_dosen,email_dosen)
    values(new.id_dosen,new.nama_dosen,new.email_dosen);
end;
delete from dosen1 where id_dosen = "D0003";
insert into dosen1(id_dosen,nama_dosen,email_dosen)
values('D0003','Dosen Testing3',"Dosen_testing3@gmail.com");

SELECT * from dosen1,dosen2;

SELECT * from dosen1;


begin try
    select 1/0 as Error;
end try
begin catch
    select
        ERROR_NUMBER() AS ErrorNumber,
        ERROR_STATE() AS ErrorState,
        ERROR_SEVERITY() AS ErrorSeverity,
        ERROR_PROCEDURE() AS ErrorProcedure,
        ERROR_LINE() AS ErrorLine,
        ERROR_MESSAGE() AS ErrorMessage;
End catch;
/* code diatas tidak dapat dijalankan */