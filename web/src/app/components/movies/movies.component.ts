import { Component, OnInit } from '@angular/core';
import { Movie } from '../../entities/movie';

@Component({
  selector: 'app-movies',
  templateUrl: './movies.component.html',
  styleUrls: ['./movies.component.scss']
})
export class MoviesComponent implements OnInit {
  
  movie: Movie = {
    id: 1,
    name: "Harry Potter y La Piedra Filosofal",    
  }

  movies: Movie[] = [
    {id: 1, name: "Harry Potter y La Piedra Filosofal"},
    {id: 2, name: "Harry Potter y La Cámara secreta"},
    {id: 3, name: "Harry Potter y El Prisionero de Azkaban"},
    {id: 4, name: "Harry Potter y El Cáliz de Fuego"},
  ]

  constructor() { }

  save(m: Movie) {
    console.log("La pelicula " + m.name + " se guardo correctamente");
    console.log(m);
  }

  ngOnInit(): void {
  }

}
