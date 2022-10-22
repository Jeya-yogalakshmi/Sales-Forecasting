import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { DataService } from '../data.service';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent implements OnInit{

  constructor(private dataService: DataService,) { }
  public val:any = [];
  public imgSubscription!: Subscription;

  ngOnInit(): void {
  }

  

}
