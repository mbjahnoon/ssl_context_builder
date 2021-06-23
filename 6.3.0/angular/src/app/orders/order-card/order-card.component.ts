import { Component, OnInit, Input,} from '@angular/core';
import {STATUSINFO} from '../../../shared/order/statusCardInfo';




@Component({
  selector: 'app-order-card',
  templateUrl: './order-card.component.html',
  styleUrls: ['./order-card.component.css']
})
export class OrderCardComponent implements OnInit {

  // possible map for the card colors, 
  //The present will depend on the status of the order.
  statusInfo = STATUSINFO;

  @Input() orderData: any;
  constructor() { }

  ngOnInit(): void {
  }

}
