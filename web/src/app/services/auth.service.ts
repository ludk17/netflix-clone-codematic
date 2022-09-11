import { HttpClient } from '@angular/common/http';

import { Injectable } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { Observable } from 'rxjs';
import { Token } from '../entities/token';
import { User } from '../entities/user';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http:HttpClient, private cookie:CookieService) { }

  login(user:User): Observable<Token> {
    return this.http
    .post<Token>('http://localhost:8080/api/token/', user)
    .pipe()
  }

  setToken(access:string): void {
    this.cookie.set("TOKEN_ACCESS_NETFLIX_CLONE", access);
  }

  getToken(): string {
    return this.cookie.get("TOKEN_ACCESS_NETFLIX_CLONE");
  }

  clearToken(): void {
    this.cookie.delete("TOKEN_ACCESS_NETFLIX_CLONE");
  }
}
