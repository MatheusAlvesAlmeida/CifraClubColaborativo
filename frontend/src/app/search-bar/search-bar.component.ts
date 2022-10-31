import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css'],
})
export class SearchBarComponent implements OnInit {
  songName = '';
  @Output() sender = new EventEmitter();

  constructor() {}

  ngOnInit(): void {}

  onEnter() {
    this.sender.emit(this.songName);
  }
}
