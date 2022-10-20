import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { SongAPI } from 'src/api/songs-api';
import { Song } from 'src/models/song';

@Injectable()
export class AppFacade {
  public constructor(private readonly songAPI: SongAPI) {}

  public getSong(song: string): Observable<Object> {
    return this.songAPI.getSong(song);
  }
}
