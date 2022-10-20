import { Component, OnInit } from '@angular/core';
import { AppFacade } from 'src/app/app-facade';

@Component({
  selector: 'app-cifra-card',
  templateUrl: './cifra-card.component.html',
  styleUrls: ['./cifra-card.component.css'],
})
export class CifraCardComponent implements OnInit {
  constructor(private readonly appFacade: AppFacade) {
    this.appFacade.getSong('Help').subscribe((response) => {
      console.log('ENTROU');
      console.log(response.toString());
    });
  }

  ngOnInit(): void {}
}
