import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { DataService } from '../data.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent implements OnInit {

  loading: boolean = false; // Flag variable
  file= File; // Variable to store file

  public form = new FormGroup({
    file: new FormControl(''),
    period: new FormControl('', [Validators.required]),
    date: new FormControl('', [Validators.required]),
  });

  constructor(
    private dataService: DataService,
    private router: Router) { }
  getFile($event: any){
    this.file = $event.target.files[0]
    console.log("file",this.file)
  }
// OnClick of button Upload
  public onUpload(data: any) {
    console.log(this.file.name);
    console.log(this.form.controls.period.value);
    console.log(this.form.controls.date.value);
    this.dataService.values(data, this.file).subscribe(data=>{
      this.router.navigate(['/result']);
    })
    this.loading = !this.loading;
}
ngOnInit(): void {}
}
