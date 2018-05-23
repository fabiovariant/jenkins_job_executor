CREATE DATABASE jenkins_executor;
USE jenkins_executor;

-- Tabela que irá listar tipos de usuários.
CREATE TABLE Dm_User_type (
    cd_user_Type        varchar(5)      NOT NULL,
    ds_user_type        varchar(100),
    CONSTRAINT Pk_user_type PRIMARY KEY (cd_user_Type)
);

-- Tabela que com dados de usuários.
CREATE TABLE user (
    id                  int(10)         NOT NULL AUTO_INCREMENT,
    nm_User             varchar(50)     NOT NULL,
    nm_Email            varchar(50)     NOT NULL,
    user_password       varchar(250)    NOT NULL,
    cd_user_Type        varchar(5)      NOT NULL,
    is_Blocked          boolean,
    CONSTRAINT Pk_user PRIMARY KEY (id, nm_Email),
    CONSTRAINT uc_email UNIQUE (nm_Email),
    FOREIGN KEY (cd_user_Type) REFENCES Dm_User_type(cd_user_Type),
    PRIMARY KEY(id, nm_User, nm_Email)
);

-- Tabela com lista de jobs
CREATE TABLE job (
    id_job              int(10)         NOT NULL AUTO_INCREMENT,
    nm_Job              varchar(50)     NOT NULL,
    job_param           VARCHAR(4000)   NOT NULL,
    PRIMARY KEY(id_job, nm_Job)
    CONSTRAINT uc_nm_job UNIQUE (nm_Job),
);

-- Tabela com tipos de permissão em jobs.
CREATE TABLE job_user_permission (
    id_job              int(10)         NOT NULL,
    cd_user_Type        varchar(5)      NOT NULL,
    PRIMARY KEY(id_job, cd_user_Type),
    FOREIGN KEY (id_job) REFENCES job(id),
    FOREIGN KEY (cd_user_Type) REFENCES Dm_User_type(cd_user_Type)
);

-- Não tem FK com a Job pois um Job pode deixar de existir.
CREATE TABLE job_exec_history (
    id_exec                 int(10)         NOT NULL AUTO_INCREMENT,
    id_user                 int             NOT NULL,
    job_name                int             NOT NULL,
    dt_exec                 TIMESTAMP       NOT NULL DEFAULT NOW(),
    exec_return             VARCHAR(4000),
    sucess                  boolean,
    finished                boolean,
    PRIMARY KEY (id_exec, id_user, job_name),
    FOREIGN KEY (id_user) REFENCES user(id),
);
