import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Movie } from '../entities/movie';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class MovieService {

  constructor(private http:HttpClient, private auth: AuthService) {}

  getMovies(): Observable<Movie[]>{
    const url = environment.api_url + '/api/movies';
    
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + this.auth.getToken()
    })
    
    return this.http
    .get<Movie[]>(url, {headers:headers})
    .pipe()
  }
}

// http://localhost:8080?name=1