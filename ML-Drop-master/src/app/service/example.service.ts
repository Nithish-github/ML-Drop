import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ExampleService {
  private apiUrl = 'http://localhost:8000/api/example/';

  constructor(private http: HttpClient) {}

  getExampleData(): Observable<any> {
    return this.http.get(this.apiUrl);
  }
}
