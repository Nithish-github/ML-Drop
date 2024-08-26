import { ChangeDetectionStrategy, Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import {
  MatDialogActions,
  MatDialogClose,
  MatDialogContent,
} from '@angular/material/dialog';

@Component({
  selector: 'app-dialog',
  standalone: true,
  templateUrl: './dialog.component.html',
  styleUrl: './dialog.component.scss',
  imports: [
    MatDialogContent,
    MatDialogActions,
    MatDialogClose,
    MatButtonModule,
  ],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DialogComponent {}
