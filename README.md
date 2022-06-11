# TicketSystem w/ Django

## Environment
1. Python3
2. Django 4.0.5

## Usage
### Login URL
```http://[your ip]:[port]/ticket```

### Test Accouts & Password
* ```RD``` / ```rd123456```
* ```QA``` / ```QA123456```
* ```PM``` / ```pm123456```
* ```ADMIN``` / ```admin123456```

### Phase I usage flow
1. QA Creates ticket by filling in [New Ticket] page
1. RD switches ticket to "Resolve"
1. QA can swith to [Close] if QA acknowledges. If not, QA may switch back to [Open]

### Phase II usage flow

## System Architecture
* User
  - Uses django default model
  - Groups including: RD, QA, PM, 
* Ticket Class
  - title (string)
  - description (string)
  - status (enum)
  - t_type (enum)
  - severity (enum)
  - creator (django User class)
  - create_date (datetime)
* Pages
  - Login
  - Ticket List
  - Ticket Detail

## API Implementation Plan
* Authentication with access token in header

```
get_tickets()
```
```
get_ticket(int id)
```
```
create_ticket(Ticket ticket)
```
```
modify_ticket(int id, Ticket new_ticket)
```
