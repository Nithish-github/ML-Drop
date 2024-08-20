import { CdkDrag, CdkDragEnd } from '@angular/cdk/drag-drop';
import { AfterViewInit, Component, Input, OnInit } from '@angular/core';
import { BlockManagerService } from '../service/block-manager.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-block',
  standalone: true,
  imports: [CdkDrag, CommonModule],
  templateUrl: './block.component.html',
  styleUrl: './block.component.scss',
})
export class BlockComponent implements OnInit, AfterViewInit {
  position = { x: 0, y: 0 };
  initialPosition = { x: 0, y: 0 };
  isDragging: boolean = false;
  public controlId!: string;

  @Input() blockId!: number;

  constructor(private _blockManagerService: BlockManagerService) {
    this._blockManagerService.blockCount++;
  }

  public ngOnInit() {
    this.controlId = 'control_' + this.blockId;
  }

  public ngAfterViewInit(): void {
    this._blockManagerService.$isNewBlockPushed.next(true);
  }
}
