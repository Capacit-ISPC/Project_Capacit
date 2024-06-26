import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule} from '@angular/forms';

import { AppComponent } from './app.component';
import { FooterComponent } from './footer/footer.component';
import { RegisterComponent } from './register/register.component';
import { HeaderComponent } from './header/header.component';
import { CarritoComponent } from './carrito/carrito.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { NavbarComponent } from './navbar/navbar.component';
import { PerfilComponent } from './perfil/perfil.component';
import { HomeComponent } from './home/home.component';
import { NoticiasComponent } from './noticias/noticias.component';
import { CursosComponent } from './cursos/cursos.component';
import { RutasComponent } from './rutas/rutas.component';
import { LoginComponent } from './login/login.component';
import { CourseCardComponent } from './course-card/course-card.component';
import { RoutesAddressComponent } from './routes-address/routes-address.component';
import { PasswordComponent } from './password/password.component';
import { ContactFormComponent } from './contact-form/contact-form.component';
import { AboutUsComponent } from './about-us/about-us.component';
import { CourseDetailComponent } from './course-detail/course-detail.component';
import { NuestraAppComponent } from './nuestra-app/nuestra-app.component';



@NgModule({
  declarations: [
    AppComponent,
    FooterComponent,
    RegisterComponent,
    HeaderComponent,
    PageNotFoundComponent,
    NavbarComponent,
    PerfilComponent,
    CarritoComponent,
    HomeComponent,
    NoticiasComponent,
    CursosComponent,
    RutasComponent,
    LoginComponent,
    CourseCardComponent,
    RoutesAddressComponent,
    PasswordComponent,
    ContactFormComponent,
    AboutUsComponent,
    CourseDetailComponent,
    NuestraAppComponent,

  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
