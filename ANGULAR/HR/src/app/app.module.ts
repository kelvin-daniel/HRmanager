import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { SignupComponent } from './signup/signup.component';
import { LoginComponent } from './login/login.component';
import { HrmanagerService } from './hrmanager.service';
import { HrmanageradminComponent } from './hrmanageradmin/hrmanageradmin.component';
import { CompanyadminComponent } from './companyadmin/companyadmin.component';
import { TeammanagerComponent } from './teammanager/teammanager.component';
import { UserComponent } from './user/user.component';
import { AddEditUserComponent } from './hrmanageradmin/add-edit-user/add-edit-user.component';
import { AddEditTeamComponent } from './companyadmin/add-edit-team/add-edit-team.component';
import { ApplyLeaveComponent } from './user/apply-leave/apply-leave.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    SignupComponent,
    LoginComponent,
    HrmanageradminComponent,
    CompanyadminComponent,
    TeammanagerComponent,
    UserComponent,
    AddEditUserComponent,
    AddEditTeamComponent,
    ApplyLeaveComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule,
    HttpClient,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [HrmanagerService],
  bootstrap: [AppComponent]
})
export class AppModule { }
