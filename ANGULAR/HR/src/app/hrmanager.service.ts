import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

@Injectable({
  providedIn: 'root'
})
export class HrmanagerService {
  readonly APIUrl = "http://localhost:8000";

  constructor(private http: HttpClient) { }

  signup(data: any){
    return this.http.post(`${this.APIUrl}/signup/`, data);
  }

  login(data: any) {
    return this.http.post(`${this.APIUrl}/login/`, data);
  }
}
