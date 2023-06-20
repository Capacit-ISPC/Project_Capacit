import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { User } from "../Models/User";

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private url:string = 'http://127.0.0.1:8000/api/capacit/'

  constructor(private http: HttpClient) {}

  registrarUsuario(user: User): Observable<any> {
    return this.http.post(this.url + "create/", user);
  }

  login(user: User): Observable<any>{
    return this.http.post(this.url + "token/",user);
  }

  logout(){

  }
}
