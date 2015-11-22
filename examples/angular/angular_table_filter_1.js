<tr><td><input ng-model="f.name"></td><td><input ng-model="f.distance"></td></td><td><input ng-model="f.mass"></td></tr>
<tr ng-repeat="p in planets | filter:f"><td>{{p.name}}</td><td>{{p.distance}}</td><td>{{p.mass}}</td></tr>

