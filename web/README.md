# Web

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 14.0.1.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.



## Despliegue WEB / Interfaz
1. modificar archivo environment.prod.ts colocar servidor y puerto correcto
2. Ejecutar comando (reemplazar lo que sea necesario)
```
ng build --configuration=production --base-href=/luigui/
```
3. Zip dist/web 
4. copiar al server
```
scp -i /ruta/llave-seguridad.pem archivo-copiar.zip usuario@ip-server:/tmp
```
5. descomprimir en /var/www/html
```
mv /tmp/nombre-archivo.zip /var/www/html
cd /var/www/html
unzip /tmp/nombre-archivo.zip 
```

### Deplegar application
1. Comprimir todo menos env folder
2. Copiar al servidor y descomprimir en cualquier lugar
3. Instalar requirements.txt
```
pip install -r requirements
```
4. Instalar gunicorn
```
pip install gunicorn
```
5. Iniciar application
```
gunicorn nombre_app.wsgi --bind=0.0.0.0:<port>
```
