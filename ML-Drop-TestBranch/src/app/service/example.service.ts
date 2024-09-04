import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';


interface ExampleResponse {
  message: string;
  image_data: string; // Base64 encoded image data
}


@Injectable({
  providedIn: 'root',
})


export class ExampleService {
  private apiUrl = 'http://localhost:8000/challenge/api/example/';

  constructor(private http: HttpClient) {}

  getExampleData(): Observable<ExampleResponse> {
    return this.http.get<ExampleResponse>(this.apiUrl);
  }
}
