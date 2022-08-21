import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Movie } from '../entities/movie';

@Injectable({
  providedIn: 'root'
})
export class MovieService {

  constructor(private http:HttpClient) {}

  getMovies(): Observable<Movie[]>{
    const url = 'http://127.0.0.1:8000/api/movies';
    
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + 'askdaskdasdalsdnasdk'
    })
    
    return this.http
    .get<Movie[]>(url, {headers:headers})
    .pipe()
  }
}

// http://localhost:8080?name=1