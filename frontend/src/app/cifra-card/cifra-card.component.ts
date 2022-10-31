import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { AppFacade } from 'src/app/app-facade';
import { SearchBarComponent } from '../search-bar/search-bar.component';

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
export class CifraCardComponent {
  song: Array<Song> = [];
  chord: any;
  @Input() songToSearch: string = '';

  constructor(private readonly appFacade: AppFacade) {}

  ngOnChanges() {
    this.searchSong();
  }

  searchSong() {
    this.appFacade.getSong(this.songToSearch).subscribe((response) => {
      this.song = Object.values(response)[0];
      this.appFacade.getChord(this.song).subscribe((response) => {
        this.chord = response;
      });
    });
  }
}
