import { Component, OnInit } from '@angular/core';
import { AppFacade } from 'src/app/app-facade';

@Component({
  selector: 'app-cifra-card',
  templateUrl: './cifra-card.component.html',
  styleUrls: ['./cifra-card.component.css'],
})
export class CifraCardComponent implements OnInit {
  constructor(private readonly appFacade: AppFacade) {
    this.appFacade.getSong('teste').subscribe((response) => {
      console.log(response);
    });
  }

  ngOnInit(): void {}
}
