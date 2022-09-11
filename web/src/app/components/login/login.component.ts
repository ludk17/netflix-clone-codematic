import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { User } from 'src/app/entities/user';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  user = {} as User;

  constructor(private service: AuthService, private router: Router) { }

  ngOnInit(): void {
  }

  login(user:User): void {
    this.service.login(user)
      .subscribe(token => {
        console.log(token);
        this.service.setToken(token.access);
        this.router.navigate(['/']);
      });
  }

}
