import {Routes} from '@angular/router';
import {GptComponent} from "./gpt/gpt.component";

export const routes: Routes = [
  {path: 'gpt', component: GptComponent},
  {path: '', redirectTo: '/gpt', pathMatch: 'full'}
];
