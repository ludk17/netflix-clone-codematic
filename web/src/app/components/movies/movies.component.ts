import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { MovieService } from 'src/app/services/movie.service';
import { Movie } from '../../entities/movie';

@Component({
  selector: 'app-movies',
  templateUrl: './movies.component.html',
  styleUrls: ['./movies.component.scss']
})
export class MoviesComponent implements OnInit {

  movies: Movie[] = []

  constructor(private service:MovieService, private auth: AuthService, private router: Router) { }

  ngOnInit(): void {

    this.service.getMovies()
    .subscribe(data => {
      this.movies = data;
    })
  }

  logout() {
    console.log("logout");
    this.auth.clearToken();
    this.router.navigate(["/login"]);
  }

}
