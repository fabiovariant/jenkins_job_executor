USE jenkins_executor;

-- Insere tipos de usuário
INSERT INTO Dm_User_type(cd_user_Type, ds_user_type) VALUES ('ROOT', 'Usuário que pode cadastrar outros usuários e alterar seus dados.');
INSERT INTO Dm_User_type(cd_user_Type, ds_user_type) VALUES ('WORK', 'Usuário que pode apenas executar jobs.');
