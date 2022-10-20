import { Component, OnInit } from '@angular/core';
import { AppFacade } from 'src/app/app-facade';

// song type
interface Song {
  artist: Artist;
  genre: Genre;
  name: string;
  slug: string;
}

interface Artist {
  name: string;
  slug: string;
}

interface Genre {
  name: string;
  url: string;
}

@Component({
  selector: 'app-cifra-card',
  templateUrl: './cifra-card.component.html',
  styleUrls: ['./cifra-card.component.css'],
})
export class CifraCardComponent implements OnInit {
  song: Array<Song> = [];
  chord: any;

  constructor(private readonly appFacade: AppFacade) {}
  ngOnInit(): void {
    this.appFacade.getSong('anunciacao').subscribe((response) => {
      this.song = Object.values(response)[0];
      this.appFacade.getChord(this.song).subscribe((response) => {
        this.chord = response;
      });
    });
  }
}
