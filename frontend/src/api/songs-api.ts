import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { retry, map } from 'rxjs/operators';
import { Observable, ObservableLike } from 'rxjs';

@Injectable()
export class SongAPI {
  private headers = new HttpHeaders({
    'Content-Type': 'application/json',
  });
  private baseUrl = 'http://localhost:3000';

  public constructor(private readonly http: HttpClient) {}

  public getSong(song: string) {
    return this.http
      .get(`${this.baseUrl}/songs/${song}`, {
        headers: this.headers,
      })
      .pipe(
        retry(3),
        map((response: any) => response)
      );
  }
  public getChord(song: any) {
    return this.http
      .get(`${this.baseUrl}/chords/${song.artist.slug}/${song.slug}`, {
        headers: this.headers,
      })
      .pipe(
        retry(3),
        map((response: any) => response)
      );
  }
}
