import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { SignupComponent } from './signup/signup.component';
import { LoginComponent } from './login/login.component';
import { HrmanageradminComponent } from './hrmanageradmin/hrmanageradmin.component';
import { CompanyadminComponent } from './companyadmin/companyadmin.component';
import { TeammanagerComponent } from './teammanager/teammanager.component';
import { UserComponent } from './user/user.component';

const routes: Routes = [
  {path:'home',component:HomeComponent},
  {path:'signup',component:SignupComponent},
  {path:'login',component:LoginComponent},
  {path:'hrmanageradmin',component:HrmanageradminComponent},
  {path:'companyadmin',component:CompanyadminComponent},
  {path:'teammanager',component:TeammanagerComponent},
  {path:'user',component:UserComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
