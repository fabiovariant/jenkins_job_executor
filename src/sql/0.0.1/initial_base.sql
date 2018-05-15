CREATE DATABASE jenkins_executor;
USE jenkins_executor;

CREATE TABLE Dm_User_type (
    cd_user_Type        varchar(5)      NOT NULL,
    ds_user_type        varchar(100),
    CONSTRAINT Pk_user_type PRIMARY KEY (cd_user_Type)
);

INSERT INTO Dm_User_type(cd_user_Type, ds_user_type) VALUES ('ROOT', 'Usuário que pode cadastrar outros usuários e alterar seus dados.')
INSERT INTO Dm_User_type(cd_user_Type, ds_user_type) VALUES ('WORK', 'Usuário que pode apenas executar jobs.')

CREATE TABLE user (
    id                  int(10)         unsigned NOT NULL AUTO_INCREMENT,
    nm_User             varchar(50)     NOT NULL,
    nm_Email            varchar(50)     NOT NULL,
    user_password       varchar(250)    NOT NULL,
    cd_user_Type        varchar(5)      NOT NULL,
    is_Blocked          boolean,
    CONSTRAINT Pk_user PRIMARY KEY (id, nm_Email),
    CONSTRAINT uc_email UNIQUE (nm_Email),
    FOREIGN KEY (cd_user_Type) REFENCES Dm_User_type(cd_user_Type)
);

