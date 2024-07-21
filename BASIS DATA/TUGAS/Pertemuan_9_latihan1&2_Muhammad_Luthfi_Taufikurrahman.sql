CREATE DATABASE PERTEMUAN9;

USE PERTEMUAN9;

/* latihan 1*/

CREATE TABLE DOSEN1
(
    ID_DOSEN VARCHAR(5) PRIMARY KEY,
    NAMA_DOSEN VARCHAR(50),
    EMAIL_DOSEN VARCHAR(50)
);

CREATE TABLE KULIAH1
(
    ID_KULIAH VARCHAR(5) PRIMARY KEY,
    NAMA_KULIAH VARCHAR(255),
    SKS int,
    ID_DOSEN varchar(5),
    foreign key (ID_DOSEN) references DOSEN1(ID_DOSEN)
);

/* latihan 2 */

CREATE TABLE DOSEN2
(
    ID_DOSEN VARCHAR(5) PRIMARY KEY,
    NAMA_DEPAN_DOSEN VARCHAR(50),
    NAMA_BELAKANG_DOSEN VARCHAR(50),
    NAMA_DOSEN VARCHAR(200) as (CONCAT(NAMA_DEPAN_DOSEN,"",NAMA_BELAKANG_DOSEN)),
    EMAIL_DOSEN VARCHAR(200)
);

CREATE TABLE KULIAH2
(
    ID_KULIAH VARCHAR(5) PRIMARY KEY,
    NAMA_KULIAH VARCHAR(255),
    SKS int
);

CREATE TABLE RELASI2
(
    ID_DOSEN VARCHAR(5),
    ID_KULIAH VARCHAR(5),
    foreign key (ID_DOSEN) references DOSEN2(ID_DOSEN),
    foreign key (ID_KULIAH) references KULIAH2(ID_KULIAH)
);

/* Testing */

insert into DOSEN1
VALUES
('D0001','Dosen Testing','Dosen_testing@gmail.com'),
('D0002','Dosen Testing2','Dosen_testing2@gmail.com');

INSERT into KULIAH1
VALUES
('K0001','Kuliah Testing', 2,'D0002'),
('K0002','Kuliah Testing2', 4,'D0001');

SELECT * FROM DOSEN1;
SELECT * FROM KULIAH1;

insert into DOSEN2(ID_DOSEN,NAMA_DEPAN_DOSEN,NAMA_BELAKANG_DOSEN,EMAIL_DOSEN)
VALUES
('D0001','Dosen','Testing','Dosen_testing@gmail.com'),
('D0002','Dosen','Testing2','Dosen_testing2@gmail.com');

INSERT into KULIAH2
VALUES
('K0001','Kuliah Testing', 2),
('K0002','Kuliah Testing2', 4);

insert into RELASI2
values
('D0001','K0002'),
('D0001','K0001'),
('D0002','K0001');

SELECT * FROM dosen2;
SELECT * FROM kuliah2;
SELECT * FROM relasi2;


