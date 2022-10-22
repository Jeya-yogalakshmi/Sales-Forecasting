import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { ResultComponent } from './result/result.component';
import { UploadComponent } from './upload/upload.component';

const routes: Routes = [
  { path:'',redirectTo:'login',pathMatch:'full'},
  { path: 'upload', component: UploadComponent },
  { path: 'result', component: ResultComponent },
  { path: 'login', component: LoginComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
