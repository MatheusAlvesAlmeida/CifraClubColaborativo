import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { CifraCardComponent } from './cifra-card/cifra-card.component';

import { AppFacade } from './app-facade';
import { SongAPI } from 'src/api/songs-api';

@NgModule({
  declarations: [AppComponent, CifraCardComponent],
  imports: [BrowserModule, AppRoutingModule, HttpClientModule],
  providers: [AppFacade, SongAPI],
  bootstrap: [AppComponent],
})
export class AppModule {}
