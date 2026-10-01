@ECHO OFF
echo Iniciando deploy...

if not exist "C:\Docker\DockerDeplyDB\SQLServerDB\volume" mkdir C:\Docker\DockerDeplyDB\SQLServerDB\volume

timeout 0
docker-compose up -d

timeout 10
docker container ls

timeout 5
echo Creando BD
sqlcmd -S localhost,1433 -U sa -P Password_01 -i C:\Docker\DockerDeplyDB\SQLServerDB\DB.sql

timeout 5
echo Creando tablas
sqlcmd -S localhost,1433 -U sa -P Password_01 -i C:\Docker\DockerDeplyDB\SQLServerDB\DB_Tables.sql -o C:\Docker\DockerDeplyDB\SQLServerDB\DB_Tables.txt

timeout 5
echo Creando Vistas y Procedimientos
sqlcmd -S localhost,1433 -U sa -P Password_01 -i C:\Docker\DockerDeplyDB\SQLServerDB\DB_Vw_Sp.sql -o C:\Docker\DockerDeplyDB\SQLServerDB\DB_Vw_Sp.txt

timeout 0
echo Deploy finalizado...
pause
