import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { retry, map } from 'rxjs/operators';
import { Observable } from 'rxjs';

@Injectable()
export class SongAPI {
  private headers = new HttpHeaders({
    'Content-Type': 'application/json',
  });
  private baseUrl = 'http://localhost:3000';

  public constructor(private readonly http: HttpClient) {}

  public getSong(song: string) {
    console.log('Entrou no getSong');
    return this.http
      .get(`${this.baseUrl}/songs/${song}`, {
        headers: this.headers,
      })
      .pipe(
        retry(3),
        map((response) => response)
      );
  }
}
