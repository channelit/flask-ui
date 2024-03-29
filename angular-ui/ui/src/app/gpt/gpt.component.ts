import {Component} from '@angular/core';
import {MatGridList, MatGridTile} from "@angular/material/grid-list";
import {MatIcon} from "@angular/material/icon";
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatInput} from "@angular/material/input";
import {RestService} from "../rest/rest.service";
import {FormsModule} from "@angular/forms";
import {JsonPipe, NgForOf} from "@angular/common";
import {MatCard, MatCardContent} from "@angular/material/card";

@Component({
  selector: 'app-gpt',
  standalone: true,
  imports: [
    MatGridList,
    MatGridTile,
    MatIcon,
    MatFormFieldModule,
    MatInput,
    FormsModule,
    NgForOf,
    JsonPipe,
    MatCardContent,
    MatCard
  ],
  templateUrl: './gpt.component.html',
  styleUrl: './gpt.component.css'
})
export class GptComponent {
  searchText: any;
  searchResult: any;

  constructor(private rest: RestService) {
  }

  onSubmit() {
    this.rest.search(this.searchText).subscribe((res: any) => {
      this.searchResult = res.pages;
      console.log(this.searchResult);
    });
  }
}
