import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

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

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    SignupComponent,
    LoginComponent,
    HrmanageradminComponent,
    CompanyadminComponent,
    TeammanagerComponent,
    UserComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule
  ],
  providers: [HrmanagerService],
  bootstrap: [AppComponent]
})
export class AppModule { }
