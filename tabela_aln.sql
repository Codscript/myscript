drop table aln;

go

create table aln(
	id_aln					INTEGER IDENTITY(1,1) CONSTRAINT PK_aln PRIMARY KEY,
	nome					VARCHAR(255) NOT NULL,
	data_de_nacimento		VARCHAR(10) NOT NULL,
	idade					INTEGER NULL,
	objetivo_da_graduacao	VARCHAR(1000) NULL,
	genero					varchar (1000) not null,
	email					varchar (1000) not null
	)
go


select * from aln