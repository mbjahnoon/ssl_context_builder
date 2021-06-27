import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { appModuleAnimation } from '@shared/animations/routerTransition';
import { MockOrdersItems } from '@shared/order/orderItem.model';
import {OrderItem} from '@shared/order/orderItem.model';
import { STATUSINFO} from '@shared/order/statusCardInfo';


@Component({
  selector: 'app-orders',
  templateUrl: './orders.component.html',
  styleUrls: ['./orders.component.css'],
  animations: [appModuleAnimation()],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class OrdersComponent implements OnInit {
  statusInfo = STATUSINFO;
  allOrdersData:OrderItem[] = null;
  ordersDataToShow:OrderItem[] = null;
  constructor() { }
  statusToShow:string = 'all';
  ngOnInit(): void { 
    this.allOrdersData = MockOrdersItems;
    this.ordersDataToShow = this.allOrdersData;
  }

  sortByStatus(newStatus:string){
    if (this.statusToShow == newStatus){ return; }
    this.ordersDataToShow = this.allOrdersData.filter(orderData => orderData > 6)
  }

}
