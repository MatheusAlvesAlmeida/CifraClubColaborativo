import { Component, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css'],
})
export class SearchBarComponent implements OnInit {
  songName = '';

  constructor() {}

  ngOnInit(): void {}

  onEnter() {
    console.log(this.songName);
  }
}
