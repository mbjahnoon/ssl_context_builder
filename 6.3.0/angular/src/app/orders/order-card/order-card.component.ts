import { Component, OnInit, Input, Output, EventEmitter, TemplateRef } from '@angular/core';
import {STATUSINFO} from '../../../shared/order/statusCardInfo';
import {OrderItem} from '../../../shared/order/orderItem.model';
import { BsModalService, BsModalRef } from 'ngx-bootstrap/modal';





@Component({
  selector: 'app-order-card',
  templateUrl: './order-card.component.html',
  styleUrls: ['./order-card.component.css']
})
export class OrderCardComponent implements OnInit {

  // possible map for the card colors, 
  //The present will depend on the status of the order.
  statusInfo = STATUSINFO;

  @Input() orderData: OrderItem;
  @Output() statusChange: EventEmitter<OrderItem> = new EventEmitter();
  modalRef: BsModalRef;
  constructor(private modalService: BsModalService) {

  }

  ngOnInit(): void {
  }
  
  openModal(template: TemplateRef<any>) {
    this.modalRef = this.modalService.show(template);
  }

}
