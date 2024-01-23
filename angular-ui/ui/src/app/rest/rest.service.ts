import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class RestService {
  private baseURL = '/api';

  constructor(private http: HttpClient) {
  }

  search(search_text: any) {
    return this.http.post(this.baseURL,
      {
        "search_text": search_text
      }
    );
  }
}
