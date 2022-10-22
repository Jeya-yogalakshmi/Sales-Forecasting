import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit(): void {
  }
  public show:boolean = false; 
  public login:boolean = true; 
  public mybutton:any = 'Show'; 
  
  public form = new FormGroup({
    email: new FormControl('', [Validators.required]),
    pwd: new FormControl('', [Validators.required]),
  });
  
  public onSubmit(): void {
    if((this.form.controls.email.value=='Jeyayoga25@gmail.com' && this.form.controls.pwd.value=="12345678") || (this.form.controls.email.value=='hello123@gmail.com' && this.form.controls.pwd.value=="hello123") || (this.form.controls.email.value=='Jeyayogalakshmi@gmail.com' && this.form.controls.pwd.value=="Jeya@25")){
      alert("Login Successful");
      this.show = !this.show;
      this.login = !this.login;
      this.router.navigate(['/upload']); 
      this.form.reset();
    }
    else{
      alert("Invalid login details")
    }
  }

}
