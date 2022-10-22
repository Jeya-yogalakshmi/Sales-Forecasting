import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private baseUrl:string = 'http://127.0.0.1:5000/result';
  constructor(private http: HttpClient) { }

  values(data: any, file:any): Observable<any>{
    const{period,date}=data;
    const formdata:FormData = new FormData();
    formdata.append("period",period);
    formdata.append("date",date);
    formdata.append("file",file ,file["filename"]);
    return this.http.post(this.baseUrl,formdata)
  }

}


