cd web
ng build --configuration=production --base-href=/luigui/
mv dist/web dist/luigui
zip dist/luigui.zip dist/luigui
scp -i ~/.ssh/angular.pem dist/luigui.zip ubuntu@34.211.197.238:/tmp
